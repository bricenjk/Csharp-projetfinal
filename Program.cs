using Microsoft.EntityFrameworkCore;

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();

// le cours -> c'est ici que l'on va config l'API

builder.Services.AddDbContext<ApplicationDbContext>(options => 
    options.UseMySql("server='127.0.0.1';uid='root';port=3306;password=mypass;database=mariadbtest",
            new MySqlServerVersion(new Version(10, 4, 0)),mySqlOptions =>
        mySqlOptions.EnableRetryOnFailure()
));


// Learn more about configuring Swagger/OpenAPI at https://aka.ms/aspnetcore/swashbuckle
builder.Services.AddEndpointsApiExplorer();
builder.Services.AddSwaggerGen();

var app = builder.Build();

// Configure the HTTP request pipeline.
if (app.Environment.IsDevelopment())
{
    app.UseSwagger();
    app.UseSwaggerUI();
}

app.UseHttpsRedirection();

app.UseAuthorization();

app.MapControllers();

app.Run();
