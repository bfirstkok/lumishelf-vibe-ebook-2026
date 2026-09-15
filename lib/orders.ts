export type OrderStatus = "PENDING" | "PAID";

export type Order = {
  id: string;
  orderNumber: string;
  bookId: string;
  customerName: string;
  customerEmail: string;
  total: number;
  status: OrderStatus;
  createdAt: string;
  downloadUrl?: string;
  downloadError?: string;
  emailStatus?: 'NOT_SENT' | 'SIMULATED' | 'SENT' | 'FAILED';
};

export function normalizeEmail(value: string) {
  return value.trim().toLowerCase();
}

export function isValidEmail(value: string) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(normalizeEmail(value));
}

export function createOrderNumber(now = new Date(), random = Math.random()) {
  const date = now.toISOString().slice(0, 10).replaceAll("-", "");
  const suffix = Math.floor(random * 36 ** 5).toString(36).toUpperCase().padStart(5, "0");
  return `LS-${date}-${suffix}`;
}

export function createDemoOrder(input: {
  bookId: string;
  customerName: string;
  customerEmail: string;
  total: number;
}): Order {
  return {
    id: crypto.randomUUID(),
    orderNumber: createOrderNumber(),
    bookId: input.bookId,
    customerName: input.customerName.trim(),
    customerEmail: normalizeEmail(input.customerEmail),
    total: input.total,
    status: "PENDING",
    createdAt: new Date().toISOString(),
  };
}
