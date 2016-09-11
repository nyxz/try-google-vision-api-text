## Testing Google's Vision API ##

Navigate to this project's directory and run

```
python generatejson.py -i resources/inputinfo.txt -o target/requests/request.json
```

to generate the request data. Then make the call to the Vision API:

```
python send-api-request.py
```

Now check the target/result folder for the result.

Note: You must have API key and set it in send-api-request.py

Some of the images are as they are, but some of them are preprocessed.

Preprocessed (binarized) with ImageMagick:

```
convert -monochrome receipt.jpg receipt-bin.jpg
```
or
```
convert receipt.jpg -threshold 10% receipt-bin.jpg
```

Preprocessed (binarized+) with GIMP: Color invert, Contrast boost, Unsharp mask, Cut to fit receipt only (no background).
