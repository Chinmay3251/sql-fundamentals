import test from "node:test";import assert from "node:assert/strict";import {retailData,summarize,validateData} from "../src/data.js";
test("sample data validates",()=>assert.equal(validateData(retailData),true));
test("KPI calculations are correct",()=>{const k=summarize(retailData);assert.equal(k.totalSales,280000);assert.equal(k.orders,1240);assert.ok(Math.abs(k.averageOrderValue-280000/1240)<1e-9);});
test("negative sales are rejected",()=>assert.throws(()=>validateData({orders:1,monthlySales:[{month:"Jan",sales:-1}],categorySales:[]}),/non-negative/));
