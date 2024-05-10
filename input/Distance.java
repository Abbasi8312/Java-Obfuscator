// Java code to compute distance

class Distance {
	// Function to calculate distance
	static double distance(int x1, int y1, int x2, int y2)
	{
		// Calculating distance
		return Math.sqrt(Math.pow(x2 - x1, 2)
						+ Math.pow(y2 - y1, 2) * 1.0);
	}
	// Driver code
	public static void main(String[] args)
	{
		System.out.println(
			Math.round(distance(3, 4, 4, 3) * 100000.0)
			/ 100000.0);
	}
}
