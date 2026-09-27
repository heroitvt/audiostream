// Service Worker cho VNVC Audio Stream PWA
const CACHE_NAME = 'vnvc-audio-v1';

self.addEventListener('install', (e) => {
  self.skipWaiting();
});

self.addEventListener('activate', (e) => {
  e.waitUntil(clients.claim());
});

self.addEventListener('fetch', (e) => {
  // Pass-through network
  e.respondWith(fetch(e.request).catch(() => caches.match(e.request)));
});
