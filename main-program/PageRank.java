import java.util.ArrayList;

public class PageRank
{
	public static final double EPSILON = Math.pow(10, (-10));
	public static final double COEF = 0.85;

	public static double calculateSumSinks(ArrayList<Vertex> sinks, int nVertices)
	{
		double sum = 0;

		for(Vertex v : sinks)
			sum += v.getPageRank();

		return sum/nVertices;
	}

	public static double calculateEpsion(ArrayList<Vertex> graph)
	{
		double epsilon = 0;

		for(Vertex v : graph)
			epsilon += Math.pow(v.getPageRank() - v.getPageRankAux(), 2);

		return Math.sqrt(epsilon);
	}

	public static ArrayList<Vertex> getSinks(ArrayList<Vertex> graph)
	{
		ArrayList<Vertex> sinks = new ArrayList<>();

		for(Vertex v : graph)
			if(v.getOutEdges().size() == 0)
				sinks.add(v);

		return sinks;
	}

	public static void calculate(ArrayList<Vertex> graph)
	{
		int nVertices = graph.size();

		double sinkSum;

		ArrayList<Vertex> sinks = getSinks(graph);

		for(Vertex v : graph)
		{
			v.setPageRankAux(0);
			v.setPageRank(1.0 / nVertices);
		}

		while(calculateEpsion(graph) > EPSILON)
		{
			sinkSum = calculateSumSinks(sinks, nVertices);

			for(Vertex v : graph)
			{
				v.setPageRankAux(v.getPageRank());
				v.setPageRank((1.0 - COEF)/nVertices + COEF*sinkSum);
			}

			for(Vertex v : graph)
				v.distributePageRank(COEF);
		}
	}
}