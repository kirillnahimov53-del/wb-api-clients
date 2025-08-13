from wbapi import WildberriesClient

if __name__ == "__main__":
    wb = WildberriesClient()
    # Подставь реальную дату/эндпоинт, это каркас
    try:
        data = wb.get_sales("2025-08-01T00:00:00Z")
        print("OK:", type(data))
    except Exception as e:
        print("ERROR:", e)
