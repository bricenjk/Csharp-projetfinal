using Microsoft.AspNetCore.Mvc;
using Microsoft.EntityFrameworkCore;
namespace apiIsitechTest.Controllers;

[ApiController]
[Route("[Controller]")]

public class HeroController : ControllerBase 
{
    private static List<Hero> heroes = new List<Hero>
    {

        new Hero {Id=1, Name = "IronMan", FirstName="Tony", LastName ="Stark"},
        new Hero {Id=2, Name = "SpiderMan", FirstName="Yves", LastName ="Saint"},
        new Hero {Id=3, Name = "Hulk", FirstName="Roger", LastName ="Milla"},
        new Hero {Id=4, Name = "Thor", FirstName="Jean", LastName ="Hugues"},
        new Hero {Id=5, Name = "SanGoku", FirstName="Baptiste", LastName ="LeBon"}
    
    };

    private readonly ApplicationDbContext _context;
    
    public HeroController(ApplicationDbContext dbContext)
    {
        this._context = dbContext;
    }

    [HttpGet]
    public async Task<ActionResult<List<Hero>>> Get()
    {
        var myHeroes = await _context.Heroes.ToListAsync();
        return Ok(heroes);
    }

    [HttpPost]
    public ActionResult Updade(Hero heroRequest)
    {
        var hero = heroes.Find(hero => heroRequest.Id == hero.Id); // lambda expression
        return Ok();
    }

    [HttpPost]

    public async Task<ActionResult<List<Hero>>> CreateHero([FromBody] Hero hero)
    {
        heroes.Add(hero);

        return Ok(heroes);
    }
}




