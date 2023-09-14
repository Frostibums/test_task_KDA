import os
from typing import Annotated

import dotenv
import requests
from fastapi import FastAPI, Query, HTTPException


dotenv.load_dotenv()
app = FastAPI()


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    """Retrieve the exchange rate between two currencies.

    Note:
        This function uses an API key (retrieved from the 'APP_ID' environment variable)
        to fetch exchange rate data from an external service.
    """
    app_id = os.getenv('APP_ID')  # Equivalent of an API key for this service
    base_url = f'https://openexchangerates.org/api/latest.json'
    request_params = {
        'app_id': app_id,
        'base': from_currency,
    }
    exchange_rates = requests.get(base_url, params=request_params).json().get('rates', None)

    if not exchange_rates:
        raise HTTPException(status_code=404, detail=f'Failed to fetch {from_currency} exchange rates!')

    if to_currency not in exchange_rates:
        raise HTTPException(status_code=404, detail=f'Currency {to_currency} not found in {from_currency} rates list!')

    return exchange_rates.get(to_currency)


@app.get("/api/rates", response_model=dict)
async def convert_currency(from_currency: Annotated[str, Query(alias='from', max_length=3)],
                           to_currency: Annotated[str, Query(alias='to', max_length=3)],
                           value: float = 1.0):

    exchange_rate = get_exchange_rate(from_currency.upper(), to_currency.upper())
    converted_value = round(value * exchange_rate, 2)
    return {"result": converted_value}
