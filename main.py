from exif import Image
def jpg_to_exif(a):
    with open(a, "rb") as img_file:
        img = Image(img_file)
    if img.has_exif:
        print(f"EXIF data found in {a}.")
    else:
        print(f"EXIF data not found in {a}.")
    return img


def clear_all_exif(img):
    img.delete_all()
    with open("example_no_exif.jpg", "wb") as new_img_file:
        new_img_file.write(img.get_file())

def list_all_exif(img):
    print("//////////////////////////////////////////")
    for attr in img.list_all():
        try:
            value = getattr(img, attr)
            print(f"{attr}: {value}")
        except Exception:
            print(f"{attr}: failed to get value.")
    print("//////////////////////////////////////////")

def change_exif(img):
    attr = input("\nEnter the attribute name you want to change: ")

    if hasattr(img, attr):
        print(f"Current value of '{attr}': {getattr(img, attr)}")
        oldvalue = getattr(img, attr)
        while True:
            value = input("Enter the value you want to assign to the attribute: ")

            try:
                setattr(img, attr, value)
                getattr(img,attr) # when calls it will raise an exception if value is invalid
                print(f"Attribute '{attr}' updated to: {value}.")
                break  
            except ValueError as ve:
                print(f"Invalid value for attribute '{attr}': {ve}. Try again.")
                setattr(img, attr, oldvalue)
            except Exception as e:
                print(f"Failed to update attribute '{attr}': {e}. Try again.")
    else:
        print(f"The image does not have an attribute '{attr}'. Try again.")
        change_exif(img)  




img =jpg_to_exif("C:\projects\image.jpg")

list_all_exif(img)