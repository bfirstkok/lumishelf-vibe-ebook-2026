"use client";

import type { Order } from "./orders";

const KEY = "lumishelf-demo-orders-v1";

export function getDemoOrders(): Order[] {
  if (typeof window === "undefined") return [];
  try { return JSON.parse(localStorage.getItem(KEY) || "[]") as Order[]; }
  catch { return []; }
}

export function saveDemoOrder(order: Order) {
  const orders = getDemoOrders().filter((item) => item.id !== order.id);
  localStorage.setItem(KEY, JSON.stringify([order, ...orders]));
}

export function findDemoOrder(orderNumber: string, email?: string) {
  return getDemoOrders().find((order) =>
    order.orderNumber.toLowerCase() === orderNumber.trim().toLowerCase() &&
    (!email || order.customerEmail === email.trim().toLowerCase())
  );
}
