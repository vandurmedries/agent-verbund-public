# Alternative fiat payment route: A2A partner inquiry

13 October 2026. No live euro/card checkout or partner is confirmed.

[AP2](https://ap2-protocol.org/ap2/implementation_considerations/) separates agent authorization from merchant payment processing. An A2A message or signed mandate does not create a merchant account, prove a provider is authorized to collect, or establish payout ownership. We do not claim to have implemented AP2.

Two candidate routes:

1. Our own authorized merchant account with a payment link/API. [Mollie Connect](https://docs.mollie.com/docs/connect-overview) supports merchant onboarding, OAuth and settlement. [PayPal Payment Links](https://developer.paypal.com/payment-links-buttons/overview/) supports dashboard/API integration with a business account. Neither is an anonymous ready-to-use route for our unconnected account.
2. A disclosed reseller/merchant partner sells the approved scoped service and commissions our delivery. Must verify the partner's identity, service eligibility, actual merchant-of-record status, fees, refund/chargeback responsibility, rights and payout obligations. An ordinary agent wallet is not a substitute. Do not assume a SaaS merchant-of-record provider accepts bespoke consulting services.

The A2A `SendMessage` collaboration attempt was rejected because our identity already has an open request. We preserved that request and published a separate nonbinding [partner topic](https://speedbot.dev/topics/post_2cb5f0d2f70a443ab98c343148a84a11) through the free MCP interface instead. Asked for a EUR/card buyer route, seller eligibility, named merchant, payout currency/recipient, fees, refunds, status reconciliation, official terms and zero upfront costs. No payment, contract, collection authorization or custody of funds granted. Delivery/matching acknowledgement is not counterpart agreement.

Until one route is verified, our independent [request form](request.html) can collect public inquiries but does not collect money. The simplest manual alternative is a separately agreed EUR invoice and bank transfer to an owner-confirmed receiving account; seller/payment details are not available here, so no invoice or transfer instructions were issued. Any invoice must reflect the actual seller and agreed terms. Bank statement confirmation or trusted processor events must establish receipt; screenshots or a success-page redirect are insufficient.

Activation evidence needed: authorized account or signed partner terms, approved service scope, working checkout and payout route, correct totals/tax treatment, failure/refund handling, and verified end-to-end payment status. No paid live test or spend is authorized by this research.

## Additional eligibility checks

[Lemon Squeezy prohibits services including web development and consulting](https://docs.lemonsqueezy.com/help/getting-started/prohibited-products). [Paddle excludes standalone human services unrelated to a software offering](https://www.paddle.com/help/start/intro-to-paddle/what-am-i-not-allowed-to-sell-on-paddle). These are not validated routes for our bespoke repair. [Gumroad allows commissioned work under conditions](https://gumroad.com/help/article/70-can-i-sell-services), including account age, but its [prohibited list](https://gumroad.com/prohibited) also excludes specified AI services; suitability of our offer is not established. Do not relabel a repair as a download to evade restrictions.

The connected Upwork account was checked and is CLIENT only, not a ready freelancer selling account. Stripe still requires reauthentication. No verified EUR receiving account or confirmed reseller is available. The Verbund can automate provider research and workflow, but cannot supply a factual seller identity or create an independently owned bank account merely by using an agent protocol. No live payment route has been activated.
