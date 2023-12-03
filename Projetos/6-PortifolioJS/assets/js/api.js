
async function fetchProfileData(){
    const url = 'https://raw.githubusercontent.com/rafs-m1ke/dio.me/main/Projetos/PortifolioJS/assets/data/profile.json';
    const fetching = await fetch(url);
    return await fetching.json();
}