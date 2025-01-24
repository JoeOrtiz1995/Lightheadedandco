from django.http import HttpResponse


class StripeWH_Handler:
  """
  Used to handle Stripe Webhooks
  """

  def __init__(self, request):
    self.request = request

  def handle_event(self, event):
    """
    Used to handle all webhook events
    """
    return HttpResponse(content=f'Unhandled Webhook received: {event["type"]}', status=200)

  def handle_payment_intent_succeeded(self, event):
    """
    Used to handle payment_intent.succeeded webhook events
    """
    intent = event.data.object
    print(intent)
    return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)

  def handle_payment_intent_payment_failed(self, event):
    """
    Used to handle payment_intent.failed webhook events
    """
    return HttpResponse(content=f'Webhook received: {event["type"]}', status=200)