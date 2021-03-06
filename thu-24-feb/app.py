from bottle import run, get, default_app, view, post, request, redirect
import imghdr
import os
import uuid

#########################
@get("/")
@view("index")
def _():
    return


#########################
@get("/about")
@view("about")
def _():
    return


#########################
@get("/contact")
@view("contact")
def _():
    return

#########################
@get("/image-uploaded")
@view("image-uploaded")
def _():
    return

##############################
@post("/upload-image")
def _():
    image = request.files.get("image")
    # print( dir(image) )
    print(image.filename)
    file_name, file_extension = os.path.splitext(image.filename) # .png .jpeg .zip .mp4
    # print(file_name)
    # print(file_extension)
    
    # Validate extension
    if file_extension not in (".png", ".jpeg", ".jpg"):
        return "image not allowed"
    if file_extension == ".jpg" : file_extension = ".jpeg"
    
    image_id = str(uuid.uuid4())
    # Create new image name
    image_name = f"{image_id}{file_extension}"
    print(image_name)
    # Save the image
    image.save(f"images/{image_name}")

    # Make sure that the image is actually a valid image
    # by reading its mime type
    print("imghdr.what", imghdr.what(f"images/{image_name}"))   # imghdr.what png
    print("file_extension", file_extension)                     # file_extension .png
    imghdr_extension = imghdr.what(f"images/{image_name}")
    if file_extension != f".{imghdr_extension}":
        print("mmm... suspicious ... it is not really an image")
        # remove the invalid image from the folder
        os.remove(f"images/{image_name}")
        return "mmm... got you! It was not an image"

    # SUCCESS
    return redirect("/image-uploaded")

#########################
try:
    # Production server
    import production
    application = default_app()

except:
    # Development server
    run(host="127.0.0.1", port=3333, debug=True, reloader=True)