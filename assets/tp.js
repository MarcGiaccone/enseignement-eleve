// Comportements communs des TP. Chargé par <script src="../../assets/tp.js"></script>.

// Liens a[download] : le fichier est récupéré tel quel (octets identiques, donc
// métadonnées intactes) puis enregistré. En cas d'échec, le lien s'ouvre normalement.
document.querySelectorAll("a[download]").forEach(function (lien) {
  lien.addEventListener("click", function (e) {
    if (!window.fetch || !window.URL || location.protocol === "file:") { return; }
    e.preventDefault();
    fetch(lien.href)
      .then(function (r) { if (!r.ok) { throw new Error("http"); } return r.blob(); })
      .then(function (blob) {
        var url = URL.createObjectURL(blob);
        var a = document.createElement("a");
        a.href = url;
        a.download = lien.getAttribute("download");
        document.body.appendChild(a);
        a.click();
        a.remove();
        setTimeout(function () { URL.revokeObjectURL(url); }, 1000);
      })
      .catch(function () { window.location.href = lien.href; });
  });
});
