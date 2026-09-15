import OrderClient from "./order-client";

export default async function OrderPage({ params }: { params: Promise<{ id: string }> }) {
  return <OrderClient id={(await params).id} />;
}
