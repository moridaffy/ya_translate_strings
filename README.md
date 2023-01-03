# ya_translate_strings
Simple python script for automating Localizable.strings translation using Yandex Translate API

## Usage
- clone repository
- copy your main `Localizable.strings` into repository dictionary
- call `python3 ya_translate.py` with required arguments
- open output file and copy its content to your Xcode Localizable file (or just copy it to corresponding lproj directory in your project)

### Arguments
- `s` - source language code in [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) (default is `en`)
- `t` - target language code in [ISO 639-1](https://en.wikipedia.org/wiki/ISO_639-1) (default is `ru`)
- `a` - Yandex.Cloud API key which can be created [here](https://cloud.yandex.ru/docs/iam/operations/api-key/create) (default is empty)
- `f` - Yandex.Cloud folder ID which can be created [here](https://cloud.yandex.ru/docs/resource-manager/operations/folder/get-id) (default is empty)
- `v` - Verbose mode if `1` is passed (default is `0`)