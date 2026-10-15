// Shared data makes comparisons between chart libraries consistent.
export const retailData = {
  monthlySales: [
    {month:"Jan",sales:18200},{month:"Feb",sales:19500},{month:"Mar",sales:22100},
    {month:"Apr",sales:20700},{month:"May",sales:24600},{month:"Jun",sales:26300},
    {month:"Jul",sales:25100},{month:"Aug",sales:27800},{month:"Sep",sales:29100},
    {month:"Oct",sales:30400},{month:"Nov",sales:33700},{month:"Dec",sales:36500}
  ],
  categorySales: [{category:"Technology",sales:124500},{category:"Furniture",sales:87300},{category:"Office Supplies",sales:68200}],
  orders: 1240
};
export function summarize(data=retailData){
  const totalSales=data.categorySales.reduce((sum,row)=>sum+row.sales,0);
  return {totalSales,orders:data.orders,averageOrderValue:data.orders>0?totalSales/data.orders:0};
}
export function validateData(data){
  if(!data||!Array.isArray(data.monthlySales)||!Array.isArray(data.categorySales)) throw new TypeError("Expected monthlySales and categorySales arrays.");
  for(const row of [...data.monthlySales,...data.categorySales]) if(typeof row.sales!=="number"||!Number.isFinite(row.sales)||row.sales<0) throw new TypeError("Every sales value must be a finite non-negative number.");
  if(!Number.isInteger(data.orders)||data.orders<0) throw new TypeError("orders must be a non-negative integer.");
  return true;
}
