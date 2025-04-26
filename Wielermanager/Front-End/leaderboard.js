async function loadLeaderboard() {
    try {
      const response = await fetch('./leaderboard_data.json');
      const data = await response.json();
  
      const list = document.getElementById('leaderboard-list');
      list.innerHTML = ''; // Clear oude inhoud
  
      // Sorteer spelers op score
      const sorted = Object.entries(data).map(([name, info]) => ({
        name: name,
        score: info.score || 0
      })).sort((a, b) => b.score - a.score);
  
      sorted.forEach(player => {
        const item = document.createElement('div');
        item.className = 'list-item';
        item.innerHTML = `
          <div class="list-item-overlay"></div>
          <div class="list-item-content">
            <span class="item-text">${player.name}</span>
            <span class="item-score">${player.score}</span>
          </div>
        `;
        list.appendChild(item);
      });
    } catch (error) {
      console.error('Fout bij laden leaderboard:', error);
    }
  }
  
  loadLeaderboard();
  
  let playerName = ""; // Globale variabele

  function submitName() {
    const nameInput = document.getElementById('player-name'); // nu correcte id
    playerName = nameInput.value.trim();
  
    if (playerName) {
      console.log("Spelernaam:", playerName);
      alert("Welkom, " + playerName + "!");
    } else {
      alert("Vul aub eerst je naam in!");
    }
  }
  

  async function handleSubmit() {
    submitName(); // Welkom berichtje

    await submitFantasyTeam(); // Wacht totdat team is ingezonden

    await loadLeaderboard(); // Refresh het leaderboard
}


async function submitFantasyTeam() {
    const nameInput = document.getElementById('player-name');
    const playerName = nameInput.value.trim();

    if (!playerName) {
      alert("Vul aub je naam in!");
      return;
    }

    const fantasyTeam = {
      player_name: playerName,
      picks: {
        time_value: document.getElementById('time_value').value.trim(),
        coffee: document.getElementById('coffee').value.trim(),
        tires_changed: document.getElementById('tires_changed').value.trim(),
        returns: document.getElementById('returns').value.trim(),
        service_score: document.getElementById('service_score').value.trim(),
        lateness: document.getElementById('lateness').value.trim()
      }
    };

    console.log("Inzenden fantasy team:", fantasyTeam);

    try {
      const response = await fetch('http://127.0.0.1:5000/submit', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(fantasyTeam)
      });

      if (response.ok) {
        alert("✅ Inzending succesvol!");
      } else {
        alert("❌ Fout bij inzenden.");
      }
    } catch (error) {
      console.error('Fout bij verzenden:', error);
      alert("❌ Serverfout. Controleer of Flask server actief is!");
    }
}
