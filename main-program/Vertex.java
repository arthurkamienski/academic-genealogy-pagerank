import java.util.ArrayList;

public class Vertex
{
	private int number;
	private double pageRank;
	private double pageRankAux;
	private ArrayList<Vertex> outEdges;
	private ArrayList<Vertex> inEdges;

	Vertex() {}

	Vertex(int number)
	{
		this.setNumber(number);
		this.setOutEdges(new ArrayList<>());
		this.setInEdges(new ArrayList<>());
		this.setPageRank(0);
		this.setPageRankAux(0);
	}

	public void addOutEdge(Vertex vertex)
	{
		this.getOutEdges().add(vertex);
	}

	public void addInEdge(Vertex vertex)
	{
		this.getInEdges().add(vertex);
	}

	public void distributePageRank(double coef)
	{
		int outDegree = this.getOutEdges().size();
		double piece = coef*this.getPageRankAux() / outDegree;

		for(Vertex w : this.getOutEdges())
			w.addToPageRank(piece);
	}

	public void addToPageRank(double value)
	{
		this.setPageRank(this.getPageRank() + value);
	}

	public int getNumber()
	{
		return this.number;
	}

	public void setNumber(int number)
	{
		this.number = number;
	}

	public ArrayList<Vertex> getOutEdges()
	{
		return this.outEdges;
	}

	public void setOutEdges(ArrayList<Vertex> outEdges)
	{
		this.outEdges = outEdges;
	}

	public ArrayList<Vertex> getInEdges()
	{
		return this.inEdges;
	}

	public void setInEdges(ArrayList<Vertex> inEdges)
	{
		this.inEdges = inEdges;
	}

	public double getPageRank()
	{
		return this.pageRank;
	}

	public void setPageRank(double pageRank)
	{
		this.pageRank = pageRank;
	}

	public double getPageRankAux()
	{
		return this.pageRankAux;
	}

	public void setPageRankAux(double pageRankAux)
	{
		this.pageRankAux = pageRankAux;
	}
}