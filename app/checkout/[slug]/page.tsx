import { notFound } from "next/navigation";
import { getBook } from "@/lib/books";
import CheckoutForm from "./checkout-form";

export default async function CheckoutPage({ params }: { params: Promise<{ slug: string }> }) {
  const book = getBook((await params).slug);
  if (!book) notFound();
  return <CheckoutForm book={book} />;
}
