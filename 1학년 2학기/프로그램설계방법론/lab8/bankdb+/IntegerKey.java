public class IntegerKey implements Key {
	
	private int key;
	
	public IntegerKey(int i) {
		key = i;
	}
	
	public boolean equals(Key k) {
		return key == ((IntegerKey)k).getIntegerKey();
	}
	
	public int getIntegerKey() {
		return key;
	}

}


