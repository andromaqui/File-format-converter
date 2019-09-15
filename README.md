# File-format-converter

File-format-converter is a web app which allows users to convert files from one format to ther other. So far, the only features that are supported are the conversion from `CSV`to `JSON`.

The files to be converted are stored in an `AWS S3 bucket`, where they are being processed with `AWS Lambda functions`.

## TODO LIST

As the app is still under development, here are the next steps:

- [ ] Deploy project on `AWS EC2`.
- [ ] Write a CSV validator, to verify the content of the uploaded files.
- [x] Rename files with a generated `UUID` to avoid overriding in the `S3 Bucket`. 
- [x] Edit the CSS of the file upload form.
- [ ] Extend app functionality by developing features such as `JSON` to `CSV` convertion.
- [ ] Migrate SQLite to MySQL.
- [ ] Set file size limit.

