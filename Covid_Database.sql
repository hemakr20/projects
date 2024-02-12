select * from coviddeaths where continent is not null order by 3,4;

select location, date, total_cases, new_cases, total_deaths, population from coviddeaths where continent is not null order by 1,2;

# Looking for total_cases vs total_deaths
select location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_Percentage from coviddeaths where location like '%Africa%' and continent is not null order by 1,2;

# Looking for Total_cases vs Population 
# Shows what percentage of Population got covid
select location, date, total_cases, population, (total_cases/population)*100 as covid_Percentage from coviddeaths where location like '%Africa%' and continent is not null order by 1,2;

# Looking at Highest Infection rate compared to Population
select location, population, max(total_cases) as HighestInfectionCount, (max(total_cases)/population)*100 as rate_Percentage from coviddeaths where location like '%Africa%' and continent is not null group by location, population order by 1,2 ;

#showing countries with Highest Death Count per Population
select location, max(cast(total_deaths as unsigned)) as TotalDeathCount from coviddeaths where continent is not null group by location, population order by TotalDeathCount desc;

#Break down things by Continents

#showing continent with the Highest Death Count per Population
select continent, max(cast(total_deaths as unsigned)) as TotalDeathCount from coviddeaths where continent is not null group by continent order by TotalDeathCount desc;

#GLOBAL NUMBEERS
select date, total_cases, total_deaths, (total_deaths/total_cases)*100 as Death_Percentage from coviddeaths 
#where location like '%Africa%' 
where continent is not null 
order by 1,2;


select * from coviddeaths dea join covid_vaccinations vac on dea.location = vac.location and dea.date = vac.date;

# Looking at Total Populations vs Vaccinations
select dea.continent, dea.date, dea.location, dea.population, vac.new_vaccinations from coviddeaths dea 
join covid_vaccinations vac on dea.location = vac.location and dea.date = vac.date
where dea.continent is not null
order by 2,3




