int main() {
	File image;
	int choice;
	int x;
	int y;
	int imageW;
	int imageH;
	char discard;
	float pixelValue;
	
	print("Image, from 1 to 3, to draw: ");
	read(choice);
	
	print("X coordinate on screen where the drawing process will begin: ");
	read(x);
	
	print("Y coordinate on screen where the drawing process will begin: ");
	read(y);
	
	if(choice == 1) {
		open(image, "samples/imageDrawing/1.txt", 'r');
		imageW = 353 + x - 1;
		imageH = 286 + y - 1;
	}
	
	else if(choice == 2) {
		open(image, "samples/imageDrawing/2.txt", 'r');
		imageW = 431 + x - 1;
		imageH = 343 + y - 1;
	}
	
	else if(choice == 3) {
		open(image, "samples/imageDrawing/3.txt", 'r');
		imageW = 432 + x - 1;
		imageH = 358 + y - 1;
	}
	
	else {
		print("No such option ", choice, '.');
		return 0;
	}
	
	if(SCREEN_W < imageW) {
		print("Your screen width won't fit the entire drawing.", '\n', "Aborting.");
		return 0;
	}
	
	if(SCREEN_H < imageW) {
		print("Your screen height won't fit the entire drawing.", '\n', "Aborting.");
		return 0;
	}
	
	for(int currentX = x; NOT getKeyState("VK_ESCAPE") AND currentX <= imageW; currentX++) {
		count int currentY from y to imageH {
			read(image, pixelValue);
			
			if(NOT pixelValue) {
				click(currentX + x, currentY + y);
				sleep(1);
			}
		}
	}
			
	close(image, 'r');
	
	return 0;
}