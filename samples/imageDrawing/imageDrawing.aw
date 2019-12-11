int main() {
	File image;
	int choice;
	int x;
	int y;
	int imageW;
	int imageH;
	char discard;
	
	print("Image, from 1 to 1, to draw: ");
	read(choice);
	
	print("X coordinate on screen where the drawing process will begin: ");
	read(x);
	
	print("Y coordinate on screen where the drawing process will begin: ");
	read(y);
	
	if(choice == 1) {
		float pixelValue;
		open(image, "samples/imageDrawing/1.txt", 'r');
		imageW = 353 + x - 1;
		imageH = 286 + y - 1;
		
		count int currentX from x to imageW {
			if NOT getKeyState("VK_ESCAPE") {
				count int currentY from y to imageH {
					read(image, pixelValue);
					
					if(NOT pixelValue) {
						click(currentX + x, currentY + y);
					}
				}
			}
		}
	}
	
	else {
		print("No such option ", choice, '.');
	}
	
	close(image, 'r');
	
	return 0;
}