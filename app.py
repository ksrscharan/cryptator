import strategy_generator as sg


if __name__ == '__main__':
    generator = sg.GeneticAlgorithmStrateyGenerator(exchange_name='binance')
    data = generator.generate_strategy('SOLUSDT', '1d', 450)
    if data:
        arranged_data = generator.arrange_data(data)
        print(f"Successfully fetched {len(arranged_data)} candles.")
        