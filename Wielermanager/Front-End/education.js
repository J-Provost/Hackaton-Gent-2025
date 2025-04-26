const jobs = [
    "Applicatie- en databeheer", "Context 4 Omgeving en duurzame ontwikkeling", "Gezondheidszorg",
    "Optiektechnieken", "Binnenvaarttechnieken", "Defensie en veiligheid", "Muziek", "Opvoeding en begeleiding",
    "Sportwetenschappen", "Wetenschappen-Wiskunde", "Grieks-Wiskunde", "Ballet", "Project Algemene Vakken",
    "Natuurwetenschappen", "Horeca", "Freinetpedagogie", "Architectuur en interieur",
    "Biotechnologische en chemische technieken", "Informatica- en communicatiewetenschappen",
    "Taal en communicatie", "Lichamelijke Opvoeding", "Grieks/Latijn", "Moderne Vreemde Talen Frans - Engels",
    "Bakkerijtechnieken", "Rudolf Steinerpedagogie", "Beeldende vorming", "Dans", "Sport",
    "Economie-Wiskunde", "Dentaaltechnieken", "Maritieme technieken motoren", "Latijn-Moderne talen",
    "Textielontwerp en prototyping", "Bouw- en houtwetenschappen", "Yeshiva", "Crossmedia",
    "Slagerij-Traiteurtechnieken", "Topsport (dubbele finaliteit)", "Beeldende kunst", "Autotechnieken",
    "Taal en communicatiewetenschappen", "Technologische wetenschappen en engineering",
    "Textielproductietechnieken", "Wellness en schoonheid", "Welzijnswetenschappen",
    "Bedrijfsondersteunende Informaticawetenschappen", "Moderne Vreemde Talen Duits",
    "Agrotechnieken dier", "Internationale handel en logistiek",
    "Biotechnologische en chemische wetenschappen", "Mechanische vormgevingstechnieken",
    "Industriële ICT", "Context 2 Mentale gezondheid", "Context 5 Politiek-juridische samenleving",
    "Elektromechanische technieken", "Elektronicatechnieken", "Woordkunst-drama", "Podiumtechnieken",
    "Fotografie", "Commerciële organisatie", "Leren Leren", "Aardrijkskunde", "Technisch-Technologische Vorming",
    "Mechatronica", "Humane Wetenschappen", "Humane wetenschappen", "Geschiedenis", "Grafimedia",
    "Dierenverzorgingstechnieken", "Moderne talen-Wetenschappen", "Context 7 Socio culturele samenleving",
    "Moderne talen (derde graad)", "Sportbegeleiding", "Tuinaanleg en beheer", "Topsport-Wetenschappen",
    "Moderne Talen", "Economie", "Koel- en warmtetechnieken", "Bedrijfswetenschappen",
    "Architecturale vorming", "Topsport-Bedrijfswetenschappen", "Wiskunde", "Elektrotechnieken",
    "Natuur- en groentechnieken", "Toerisme", "Maritieme technieken dek", "Grieks-Latijn",
    "Orthopedietechnieken", "Audiovisuele vorming", "Stam", "Topsport", "Mode",
    "Context 3 Sociorelationele ontwikkeling", "Latijn-Wiskunde", "Context 1 Lichamelijke gezondheid en veiligheid",
    "Nederlands", "Bedrijfsorganisatie", "Agrotechnieken plant", "Wetenschappen",
    "Economie-Moderne talen", "Bouwtechnieken", "Latijn-Wetenschappen",
    "Biotechnologische en chemische STEM-wetenschappen", "Topsport-Economie",
    "Context 6 Socio-economische samenleving", "Moderne vreemde talen Frans of Engels", "Houttechnieken",
    "Vliegtuigtechnieken"
];

const jobListEl = document.getElementById("jobList");
const inputEl = document.getElementById("jobSearchInput");
const yearInputEl = document.getElementById("yearInput");


function displayJobs(filter = "") {
    const filtered = jobs
        .filter(job => job.toLowerCase().includes(filter.toLowerCase()))
        .sort();

    jobListEl.innerHTML = filtered.map(job => `<option value="${job}">${job}</option>`).join("");
}

inputEl.addEventListener("input", () => {
    displayJobs(inputEl.value);
});

yearInputEl.addEventListener("input", () => {
    console.log("Ingegeven jaar:", yearInputEl.value);
    // Hier kan je later nog iets doen met de jaarinput, zoals filteren per jaartal
});

// Initieel weergeven
displayJobs();

document.getElementById('zoekForm').addEventListener('submit', function (event) {
    event.preventDefault(); // Zorgt ervoor dat de pagina niet herlaadt
    alert('Formulier is verzonden!');
});