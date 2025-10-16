# Discord Bot with Pixiv Integration

## Installation

1. Clone the repository:
```
git clone https://github.com/Amiya0722/WaifuBot
```
2. Install the required dependencies:
```
pip install -r requirements.txt
```
3. Create a `.env` file in the project directory and add the following environment variables:
```
TOKEN=your_discord_bot_token
PIXIV_REFRESH_TOKEN=your_pixiv_refresh_token
```

## Usage

1. Run the bot:
```
python index.py
```
2. The bot will start running and you can interact with it using the following commands:
   - `@hello`: Greets the user who called the command.
   - `@waifu [tag1] [tag2] ...`: Sends a random waifu image based on the specified tags.
   - `@tag`: Displays a list of available tags for the waifu command.
   - `@helpbot`: Displays a list of available commands.
   - `@pixiv [search_term]`: Sends a random Pixiv illustration based on the specified search term.

## API

The bot uses the following APIs:
- [Discord API](https://discord.com/developers/docs/intro)
- [Waifu.im API](https://waifu.im/api-docs/)
- [Pixiv API](https://pixivpy.readthedocs.io/en/latest/)

## Contributing

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your changes to your forked repository.
5. Submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Testing

To run the tests, use the following command:
```
python -m unittest discover tests
```
