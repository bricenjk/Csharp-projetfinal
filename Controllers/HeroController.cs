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
    public async Task<ActionResult<Hero>> CreateHero(string name, string firstname, string lastname, Hero hero)
    {
        hero.Id = heroes.Count + 1;
        hero.Name = name;
        hero.FirstName = firstname;
        hero.LastName = lastname;
        _context.Heroes.Add(hero);
        await _context.SaveChangesAsync();
        return Ok(hero);
    }
    

    [HttpPut("{id}")]
    public async Task<ActionResult<Hero>> UpdateHero(int id, string name, string firstname, string lastname)
    {
        var hero = await _context.Heroes.FindAsync(id);
        if (hero == null)
        {
            return NotFound();
        }

        hero.Name = name;
        hero.FirstName = firstname;
        hero.LastName = lastname;

        _context.Heroes.Update(hero);
        await _context.SaveChangesAsync();
        return Ok(hero);
    }
    

    [HttpDelete("{id}")]
    public async Task<ActionResult<Hero>> DeleteHero(int id)
    {
        var hero = await _context.Heroes.FindAsync(id);
        if (hero == null)
        {
            return NotFound();
        }
        _context.Heroes.Remove(hero);
        await _context.SaveChangesAsync();
        return Ok(hero);
    }
    
}
