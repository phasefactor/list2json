# list2json
Create a JSON rules list from a text file of domain names.

---

Injests a list of domain names from `./input.txt` and creates `./output.txt` from the list of domain names.

Any line beginning with a `#` is considered a comment and will be ignored.

The output is in the format of a [declarativeNetRequest](https://developer.mozilla.org/en-US/docs/Mozilla/Add-ons/WebExtensions/API/declarativeNetRequest) rules list.

The rules generated simply block anything from the listed domain.
