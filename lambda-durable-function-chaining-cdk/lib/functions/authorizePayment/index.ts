interface PaymentEvent {
  orderId: string;
  customerId: string;
  paymentMethod: {
    type: "credit" | "debit";
    cardNumber: string;
    cardBrand: "Visa" | "Mastercard" | "Amex";
  };
  amount: number;
}

export async function handler(event: PaymentEvent) {
  console.log("Authorizing payment for order:", event.orderId);

  // Mock payment authorization logic
  const { paymentMethod, amount, orderId, customerId } = event;

  // Simulate payment gateway call
  const authorizationId = `AUTH-${Date.now()}-${crypto.randomUUID()}`;
  
  // Mock validation - reject if amount is too high (for demo purposes)
  if (amount > 10000) {
    return {
      orderId,
      status: "declined",
      reason: "amount_exceeds_limit",
      timestamp: new Date().toISOString(),
    };
  }

  // Mock card validation
  const lastFourDigits = String(paymentMethod.cardNumber).slice(-4);
  
  return {
    orderId,
    customerId,
    status: "authorized",
    authorizationId,
    amount,
    cardBrand: paymentMethod.cardBrand,
    lastFourDigits,
    timestamp: new Date().toISOString(),
    expiresAt: new Date(Date.now() + 7 * 24 * 60 * 60 * 1000).toISOString(), // 7 days
  };
}
