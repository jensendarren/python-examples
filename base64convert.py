import base64
imgstring = "/9j/4AAQSkZJRgABAQEAAQABAAD/2wBDAP//////////////////////////////////////////////////////////////////////////////////////wgALCAABAAEBAREA/8QAFAABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQAAAAF//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABBQJ//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQAGPwJ//8QAFBABAAAAAAAAAAAAAAAAAAAAAP/aAAgBAQABPyF//9oACAEBAAAAEH//xAAUEAEAAAAAAAAAAAAAAAAAAAAA/9oACAEBAAE/EH//2Q=="
imgdata = base64.b64decode(imgstring)
filename = 'some_image.jpg'  # I assume you have a way of picking unique filenames
with open(filename, 'wb') as f:
    f.write(imgdata)


# curl -H "Authorization: darren.jensen@gmail.com" -H "Content-Type: image/jpg" -XPOST --data ~/Desktop/@spaceB64.txt $PYAPI_TEST_URL/submit-ekyc-id-selfie