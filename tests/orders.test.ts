import assert from "node:assert/strict";
import test from "node:test";
import { createOrderNumber, isValidEmail, normalizeEmail } from "../lib/orders";

test("order number is stable and recognizable", () => {
  assert.equal(createOrderNumber(new Date("2026-09-14T10:00:00Z"), 0), "LS-20260914-00000");
  assert.match(createOrderNumber(new Date("2026-09-14T10:00:00Z"), 0.75), /^LS-20260914-[0-9A-Z]{5}$/);
});

test("email normalization protects lookups from casing and spaces", () => {
  assert.equal(normalizeEmail(" Student@Example.COM "), "student@example.com");
});

test("email validator accepts normal addresses and rejects incomplete input", () => {
  assert.equal(isValidEmail("student@example.com"), true);
  assert.equal(isValidEmail("not-an-email"), false);
  assert.equal(isValidEmail("a@b"), false);
});
