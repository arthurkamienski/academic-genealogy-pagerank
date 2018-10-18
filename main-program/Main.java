import java.util.ArrayList;
import java.io.FileNotFoundException;
import java.io.PrintWriter;

public class Main
{
	/*
	for each vertex in the graph:
	- creates a subgraph with k generations
	- calculates the pagerank
	- extract pagerank for the focus vertex
	*/
	public static void localPageRank(ArrayList<Vertex> graph, int k, String filename) throws FileNotFoundException
	{
		//makes a file - probably needs a function for that
		PrintWriter printer = new PrintWriter("PageRank-Local-" + filename + "-k=" + k + ".csv");

		ArrayList<Vertex> subgraph;

		//prints file header
		printer.println("Numero, PageRank Local, Tamanho Subgrafo");

		for(Vertex v : graph)
		{
			//to keep track (may take a while)
			System.out.print("Vertex " + v.getNumber() + "\r");

			subgraph = GraphGen.getSubgraph(v, k);

			PageRank.calculate(subgraph);

			printer.println(v.getNumber() + ", "
				+ subgraph.get(0).getPageRank() + ", "
				+ subgraph.size());
		}

		System.out.println();
		printer.close();
	}

	public static void main(String[] args) throws FileNotFoundException
	{
		// String filename = "PHDTree";
		ArrayList<Vertex> graph = GraphGen.makeFromFile(args[0]);
		// PageRank.calculate(graph);

		ArrayList<ArrayList<Vertex>> generations = Metrics.generations(graph);

		for(ArrayList<Vertex> gen : generations)
		{
			int number = generations.indexOf(gen);
			int size = gen.size();

			int inEdges = 0;
			int outEdges = 0;

			for(Vertex v : gen)
			{
				inEdges += v.getOutEdges().size();
				outEdges += v.getInEdges().size();
			}

			System.out.println(number + " & "
			 + size + " & " 
			 + inEdges + " & " 
			 + ((float) inEdges/size) + " & " 
			 + outEdges + " & " 
			 + ((float) outEdges/size));
		}

		// PrintWriter printer = new PrintWriter("PageRank-" + filename + ".csv");

		// for(Vertex v : graph)
		// 	printer.println(v.getNumber() + ", " + v.getPageRank());

		// printer.close();

		// System.out.println("PageRank Local 1");
		// localPageRank(graph, 1, filename);
		// System.out.println("PageRank Local 2");
		// localPageRank(graph, 2, filename);
		// System.out.println("PageRank Local 3");
		// localPageRank(graph, 3, filename);
		// System.out.println("PageRank Local 4");
		// localPageRank(graph, 4, filename);
		// System.out.println("PageRank Local 5");
		// localPageRank(graph, 5, filename);
	}
}