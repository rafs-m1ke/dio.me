
function updateProfileData(profileData) {
    const name = document.getElementById('profile.name');
    name.innerText = profileData.name;

    const job = document.getElementById('profile.job');
    job.innerText = profileData.job;

    const location = document.getElementById('profile.location');
    location.innerText = profileData.location;

    const phone = document.getElementById('profile.phone');
    phone.innerText = profileData.phone;
    phone.href = `https://wa.me/${profileData.phoneHref}`;




}

(async () => {

    const profileData = await fetchProfileData();
    updateProfileData(profileData);
})();