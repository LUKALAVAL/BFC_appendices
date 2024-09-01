const task_list = [
    {
        name: 'test',
        locationStart: { lng: 16.316837138193108, lat: 48.21883541203036 },
        iconStart: 'url(icons/iconDefault.png)',
        maxLoads: 10,
    },
    {
        name: 'AB',
        locationStart: { lng: 16.3140799, lat: 48.2182966 },
        locationGoal: { lng: 16.319130324194958, lat: 48.220087281066306 },
        iconStart: 'url(icons/iconA.png)',
        iconGoal: 'url(icons/iconB.png)',
        path: {
            'type': 'geojson',
            'data': {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [ [ 16.3140799, 48.2182966 ], [ 16.3151026, 48.218146 ], [ 16.3153196, 48.218773 ], [ 16.31569, 48.2192299 ], [ 16.3168442, 48.2188262 ], [ 16.3174155, 48.2187401 ], [ 16.3184242, 48.2185661 ], [ 16.3193222, 48.2184378 ], [ 16.3196654, 48.219455 ], [ 16.319336612257281, 48.219526679805945 ], [ 16.318776, 48.2196489 ], [ 16.319130324194958, 48.220087281066306 ] ]
                }
            }
        },
        maxLoads: 120,
    },
    {
        name: 'CD',
        locationStart: { lng: 16.3190267, lat: 48.2175543 },
        locationGoal: { lng: 16.315150828952724, lat: 48.221426762843926 },
        iconStart: 'url(icons/iconC.png)',
        iconGoal: 'url(icons/iconD.png)',
        path: {
            'type': 'geojson',
            'data': {
                'type': 'Feature',
                'properties': {},
                'geometry': {
                    'type': 'LineString',
                    'coordinates': [ [ 16.3190267, 48.2175543 ], [ 16.3181137, 48.2176967 ], [ 16.3170908, 48.2178465 ], [ 16.3174155, 48.2187401 ], [ 16.3168442, 48.2188262 ], [ 16.3177601, 48.2200071 ], [ 16.3166228, 48.2204065 ], [ 16.3157472, 48.2207216 ], [ 16.3148576, 48.2210475 ], [ 16.315150828952724, 48.221426762843926 ] ]
                }
            }
        },
        maxLoads: 120,
    },
]

const map_list = [
    { name: 'default', url: 'mapbox://styles/1ukq/cly2txrrj006401qpblk8fl4w' },
    { name: 'color', url: 'mapbox://styles/1ukq/clxn03tu0002301r009uu2sp4' },
]

const form_list = [
    "https://docs.google.com/forms/d/e/1FAIpQLSfkehk3bB8SLNNC-QalUgrVQwi-f4EzDsxj5d8G8ZGgbKUqgQ/viewform?usp=pp_url&entry.726004629=",
    "https://docs.google.com/forms/d/e/1FAIpQLSe4O_sIxoAKHeeGkccPWmF0mY1CRmuptEcVdURUGiKI8iUdUA/viewform?usp=pp_url&entry.726004629="
]



const UID = "id" + Math.random().toString(16).slice(2);
var task_id;
var map_id = Math.floor(Math.random() * (map_list.length)); // First map is randomly choosen
var data = [];




function startTest1() {
    // Display test interface
    document.body.className = 'test1';

    // Select test task
    task_id = 0;

    // Init map view and street view accordingly
    initMapView(task_id, map_id);
    initStreetView(task_id, map_id);
}

function startTest2() {
    // Change map
    map_id = (map_id + 1) % map_list.length;

    // Display test interface
    document.body.className = 'test2';

    // Select test task
    task_id = 0;

    // Init map view and street view accordingly
    initMapView(task_id, map_id);
    initStreetView(task_id, map_id);
}


function startTask1() {
    // Empty track
    data = [];

    // Display task1 interface
    document.body.className = 'task1';

    // Select first task
    task_id = 1;

    // Init map view and street view accordingly
    initMapView(task_id, map_id);
    initStreetView(task_id, map_id);
}

function startTask2() {
    // Empty track
    data = [];

    // Display task2 interface
    document.body.className = 'task2';

    // Select second task
    task_id = 2;

    // Init map view and street view accordingly
    initMapView(task_id, map_id);
    initStreetView(task_id, map_id);
}

function startForm1() {
    // Force street view position change to store last position
    street.setPosition({ lng: 0, lat: 0 });

    // Compress the data
    compressed = pako.deflate(JSON.stringify(data), { to: 'string' });
    compressedBase64 = btoa(String.fromCharCode.apply(null, compressed));
    console.log(compressed);
    console.log(compressedBase64);

    // Add url to iframe
    document.getElementById('iframe').src = form_list[0] + compressedBase64;

    // Display form interface
    document.body.className = 'form';


}

function startForm2() {
    // Force street view position change to store last position
    street.setPosition({ lng: 0, lat: 0 });

    // Compress the data
    compressed = pako.deflate(JSON.stringify(data), { to: 'string' });
    compressedBase64 = btoa(String.fromCharCode.apply(null, compressed));

    // Remove button for the last form
    document.getElementById('bForm').style.display = 'none';

    // Add url to iframe
    document.getElementById('iframe').src = form_list[1] + compressedBase64;

    // Display form interface
    document.body.className = 'form';
}




// MAP VIEW
function initMapView(task_id, map_id) {

    // MapboxGL token
    mapboxgl.accessToken = 'pk.eyJ1IjoiMXVrcSIsImEiOiJja3NpcDQzaDgwdTRxMnBtYjlnYnBiZXdnIn0.-yaxdG5BYguqEAe2i6JtLg';

    const map = new mapboxgl.Map({
        container: 'mapView', // Container ID
        style: map_list[map_id].url,
        minZoom: 15,
        maxBounds: [
            [16.310505728198773, 48.21608407581612],
            [16.324612988170284, 48.222919985992135]
        ]
    });

    // Add zoom and compass controls to the map
    map.addControl(new mapboxgl.NavigationControl(), 'top-left');

    // Disable rotation on map
    map.dragRotate.disable();
    map.touchZoomRotate.disableRotation();

    var task = task_list[task_id];
    var bounds = [];

    if (task.path) {
        map.on('load', () => {
            map.addSource('route', task.path);
            map.addLayer({
                'id': 'route',
                'type': 'line',
                'source': 'route',
                'layout': {
                    'line-join': 'round',
                    'line-cap': 'round'
                },
                'paint': {
                    'line-color': '#aa89d3',
                    'line-width': 7
                }
            }, 'road-label');
        });
    }


    if (task.iconStart) {
        // Create icon
        var iconStart = document.createElement('div');
        iconStart.className = 'custom-marker';
        iconStart.style.backgroundImage = task.iconStart;
        iconStart.style.width = '45px';
        iconStart.style.height = '45px';
        iconStart.style.backgroundSize = '100%';

        // Add marker to map
        var markerStart = new mapboxgl.Marker(iconStart, {
            offset: [0, -18]
        }).setLngLat(task.locationStart).addTo(map);

        // Add location to bounds
        bounds.push(markerStart.getLngLat());
    }


    if (task.iconGoal) {
        // Create icon
        var iconGoal = document.createElement('div');
        iconGoal.className = 'custom-marker';
        iconGoal.style.backgroundImage = task.iconGoal;
        iconGoal.style.width = '45px';
        iconGoal.style.height = '45px';
        iconGoal.style.backgroundSize = '100%';

        // Add marker to map
        var markerGoal = new mapboxgl.Marker(iconGoal, {
            offset: [0, -18]
        }).setLngLat(task.locationGoal).addTo(map);

        // Add location to bounds
        bounds.push(markerGoal.getLngLat());
    }


    // Center map on markers
    if (bounds.length == 1) {
        map.flyTo({
            duration: 0,
            center: bounds[0],
            zoom: 16,
        })
    }
    if (bounds.length > 1) {
        map.fitBounds(bounds, {
            duration: 0,
            padding: 50
        })
    }

}






// STREET VIEW
var street;
function initStreetView(task_id, map_id) {
    var task = task_list[task_id];
    var location = task.locationStart;
    var hpScore = 0;
    var zScore = 0;
    var panoramaCount = 1;

    // Variables to store previous heading, pitch, zoom, ts values
    var previousHeading = 34;
    var previousPitch = 10;
    var previousZoom = 0;
    var previousTimestamp = Date.now();

    // Initialize street view panoramas
    street = new google.maps.StreetViewPanorama(
        document.getElementById('streetView'), {
        position: location,
        pov: {
            heading: previousHeading,
            pitch: previousPitch,
            zoom: previousZoom
        }

    });

    // Street view options
    street.setOptions({
        showRoadLabels: false, // Hide street names on panoramas
        clickToGo: true,  // Activate movement on click
        linksControl: false // Deactivate arrows
    });



    // Function to track loaded panorama locations
    function recordPosition() {
        // Increase panorama count
        panoramaCount = panoramaCount + 1;

        // Add the position info to track
        data.push({
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [location.lng, location.lat]
            },
            "properties": {
                "heading_pitch": hpScore,
                "zoom": zScore,
                "time": Date.now() - previousTimestamp,
                "uid": UID,
                "map": map_list[map_id].name,
                "task": task_list[task_id].name,
            }
        });
        console.log(data);

        // Reset trackers
        location = { lng: street.getPosition().lng(), lat: street.getPosition().lat() };
        hpScore = 0;
        zScore = 0;
        previousTimestamp = Date.now();

        // Force quit if too many panoramas were loaded REDO
        if (panoramaCount > task.maxLoads) {
            switch(document.body.className) {
                case 'test1':
                    startTask1();
                    break;
                case 'task1':
                    startForm1();
                    break;
                case 'test2':
                    startTest2();
                    break;
                case 'task2':
                    startForm2();
                    break;
            }
        }
    }

    // Function to update explore score based on heading, pitch, and zoom changes
    function updateExploreScore() {
        var pov = street.getPov();  // Get the current Point Of View (POV)

        // Calculate the absolute differences
        var headingDiff = Math.abs(pov.heading - previousHeading);
        var pitchDiff = Math.abs(pov.pitch - previousPitch);
        var zoomDiff = Math.abs(pov.zoom - previousZoom);

        // Normalize the differences
        var normalizedHeadingDiff = headingDiff / 360;
        var normalizedPitchDiff = pitchDiff / 180;
        var normalizedZoomDiff = zoomDiff / 1;

        // Increment the explore score by the normalized differences
        hpScore += normalizedHeadingDiff + normalizedPitchDiff;
        zScore += normalizedZoomDiff;

        // Update previous values
        previousHeading = pov.heading;
        previousPitch = pov.pitch;
        previousZoom = pov.zoom;
    }

    // Record position on change
    street.addListener('position_changed', recordPosition);
    street.addListener('pov_changed', updateExploreScore);
}












