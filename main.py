import image_helpers

# Use the functions above to fetch pixel data and render the original data
url = "https://www2.eecs.berkeley.edu/Faculty/Photos/Homepages/pamelafox.jpg"
pixel_data = image_helpers.get_image_pixels(url)
image_helpers.render_pixels(pixel_data)
