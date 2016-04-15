# Yak Simulator

Collect some yaks from your area and then generate some new ones.

## Installation

```
pip install -r requirements.txt
git clone https://github.com/louis-haddrell/Yik-Yak-API
ln -s Yik-Yak-API/yikyakapi yikyakapi
```

Yeah, there's a better way to get that API, but I'm too lazy for that right now.

## Configuration

```
cp config.json.example config.json
vim config.json
```

Put your datas in there. If you don't know your user ID, omit that field. The
authentication step will ask you for a PIN from the app instead and then
print your user ID after pairing for the first time.
