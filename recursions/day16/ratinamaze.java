public class Main
{
    private boolean dfs(int[][] m, int x, int y, int n) {
        // if destination has reached
        if(x == n -1 && y == n - 1){
            return true;
        }
        
        // if the cell is blocked or already visited
        if (m[x][y] == 0) return false;
        
        // mark the cell as visited
        m[x][y] = 0;
        
        // logic 
        boolean found = false;
        
        // move to the up 
        if( x > 0 ) {
            found = dfs(m, x - 1, y, n);
        }
        // move to the down
        if(!found && x < n - 1 ) {
            found = dfs(m, x + 1, y, n);
        }
        // move to the left
        if(!found && y > 0 ) {
            found = dfs(m, x, y - 1, n);
        }
        // move the right 
        if(!found && y < n - 1) {
            found = dfs(m, x, y + 1, n);
        }
        
        // backtracking 
        // used for making a cell unmarked or unvisited
        m[x][y] = 1;
        
        return found;
    }
    public boolean canReachDestination(int[][] grid) {
        int n = grid.length;
        
        // if starting or ending position is blocked 
        // then i cant reach to the destination
        if(grid[0][0] == 0 || grid[n - 1][ n - 1] == 0){
            return false;
        }
        return dfs(grid, 0, 0, n);
    }
    
	public static void main(String[] args) {
	    Main main = new Main();
	    
		int[][] grid = {
		          {1, 0, 0, 0},
		          {1, 1, 0, 1},
		          {1, 1, 0, 0},
		          {0, 1, 1, 1}
		    };
	System.out.println(main.canReachDestination(grid));	    
	}
}
