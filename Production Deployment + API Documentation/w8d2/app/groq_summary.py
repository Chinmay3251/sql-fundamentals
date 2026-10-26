import os, re, requests

FALLBACK = ("The dataset review provides an initial view of its size, completeness, and available business measures. "
"Treat these findings as a starting point rather than proof of causation. First, investigate missing or inconsistent "
"values and confirm that the dataset covers the intended reporting period. Review numeric metrics and their ranges "
"to identify unusual values that may need validation. Where category fields are available, compare performance across "
"segments instead of relying only on overall averages. Agree on metric definitions, establish a baseline, and track "
"changes over time. Before making material operational or budget decisions, validate patterns with domain owners and "
"additional data. These steps can improve confidence in the analysis and turn initial observations into measurable "
"next actions.")

def generate_executive_summary(insights: list[str]) -> str:
    key = os.getenv('GROQ_API_KEY')
    if not key:
        return FALLBACK
    prompt = ('Using ONLY the five analytics insights below, write an executive summary of no more than 200 words. '
              'Explain business meaning, mention limitations, and suggest practical direction. Do not invent facts or causes. '
              'Return only the summary.\n\n' + '\n'.join(f'{i+1}. {x}' for i, x in enumerate(insights[:5])))
    try:
        r = requests.post('https://api.groq.com/openai/v1/chat/completions',
            headers={'Authorization': f'Bearer {key}', 'Content-Type': 'application/json'},
            json={'model': os.getenv('GROQ_MODEL', 'llama-3.3-70b-versatile'),
                  'messages': [{'role':'system','content':'Write evidence-based business summaries.'}, {'role':'user','content':prompt}],
                  'temperature':0.2, 'max_tokens':300}, timeout=30)
        r.raise_for_status()
        result = r.json()['choices'][0]['message']['content'].strip()
        words = re.findall(r"\b[\w’'-]+\b", result)
        return ' '.join(words[:200]) if words else FALLBACK
    except (requests.RequestException, KeyError, IndexError, ValueError):
        return FALLBACK
