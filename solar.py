

REST = 700
REST_Z = REST
REST_Y = -REST

STARS = {Sun:1,Mercury:2,Venus:3,Earth:4,Moon:5,Mar:6,Jupiter:7,Saturn:8,Uranus:9,Neptune:10}

class SolarSystem:
	
	def __init__(self):
		self.viewX = 0
		self.viewY = REST_Y
		self.viewZ = REST_Z
		self.centerX = 0
		self.centerY = 0
		self.centerZ = 0
		self.upX = 0
		self.upY = 0
		self.upZ = 1
		
		self.stars = np.array([])
		
		rgbColor = np.array([1.0, 0.0, 0.0], np.float32)
		self.stars[Sun] = LightPlanet(SUN_RADIUS,0,0,SELFROTATE,0,rbgColor)
		
		


