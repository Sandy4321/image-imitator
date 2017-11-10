# image directories
input_image_directory = "D:/work/training-data/images/foreground/"
background_image_directory = "D:/work/training-data/images/background/"

# save dirs
save_image_dir = "D:/work/training-data/generated/images/"
save_anno_dir = "D:/work/training-data/generated/anno/"

# generate this many training images
num_generated_images = 12000

# size of images
# input and output images will be resized to be these sizes
image_width = 640
image_height = 480
image_depth = 3

segmented = 0

num_iters_per_fg_and_bg = 1

# labels for extracted objects
class Labels:
	thumb = "thumb"
	index = "index"
	middle = "middle"
	ring = "ring"
	pinky = "pinky"

	def get_labels(self):
		return [self.thumb, self.index, self.middle, self.ring, self.pinky]