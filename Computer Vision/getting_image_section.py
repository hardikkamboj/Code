import cv2

class Image:
	def __init__(self,image_path):
		self.image = cv2.imread(image_path)
		self.height,self.width,self.channel = self.image.shape
		self.x_center = self.width //2 
		self.y_center = self.height // 2 
	
	def get_section(self,section: str):
		'''
		Returns a particular section of the image
		input: 
			section - (list)
					- values it can take - ['tl','tr','bl','br']
					('top left', 'top right', 'bottom left', 'bottom right')
		returns: 
			image 
		'''
		if section == 'tl':
			return self.image[0:self.y_center,0:self.x_center]
		
		elif section == 'tr':
			return self.image[0:self.y_center, self.x_center:self.width]
		
		elif section == 'bl':
			return self.image[self.y_center:self.height,0:self.x_center]

		else:
			return self.image[self.y_center:self.height,self.x_center:self.width]
