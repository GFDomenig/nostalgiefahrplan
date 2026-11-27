// Minimaler Service Worker: macht die Seite installierbar, lädt Inhalte immer frisch aus dem Netz.
self.addEventListener("install",()=>self.skipWaiting());
self.addEventListener("activate",e=>e.waitUntil(self.clients.claim()));
self.addEventListener("fetch",()=>{});
