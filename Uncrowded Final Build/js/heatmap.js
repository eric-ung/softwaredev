var map;
function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		zoom: 15.5,
		center: {lng: -80.733744, lat: 35.308674}
	});

	map.data.loadGeoJson('https://raw.githubusercontent.com/eric-ung/softwaredev/master/data/UNCC_heatmap.geo.json');

	function pinSymbol(color, color2) {
		return {
			path: 'M 0,0 C -2,-20 -10,-22 -10,-30 A 10,10 0 1,1 10,-30 C 10,-22 2,-20 0,0 z',
			fillColor: color,
			fillOpacity: 1,
			strokeColor: color2,
			strokeWeight: 2
		};
	}

	var pins = [
		['#00639b', '#00507c', 'Least'], 
		['#40aae6', '#239de2', 'Some'], 
		['#008a64', '#006e50', 'Average'], 
		['#eee12a', '#e2d412', 'Extra'],
		['#ba5200', '#954200', 'Most']
	]

	map.data.setStyle(function(feature) {
		var max_value = feature.getProperty('max');
		const date = new Date();
		const day = date.getDay() - 1 < 0 ? 6 : date.getDay() - 1;
		const hour = date.getHours();
		var comparison = feature.getProperty(day)[hour] / max_value;
		// debugger;
		if (comparison >= 0.8) {
			return { icon: pinSymbol(pins[4][0], pins[4][1]) }
		}
		else if (comparison >= 0.6) {
			return { icon: pinSymbol(pins[3][0], pins[3][1]) }
		}
		else if (comparison >= 0.4) {
			return { icon: pinSymbol(pins[2][0], pins[2][1]) }
		}
		else if (comparison >= 0.2) {
			return { icon: pinSymbol(pins[1][0], pins[1][1]) }
		}
		else {
			//console.log(icon_url + '0.svg')
			return { icon: pinSymbol(pins[0][0], pins[0][1]) } 
		}
	});

	var infowindow = new google.maps.InfoWindow();

	map.data.addListener('click', function(event) {
		//document.getElementById('info-box').textContent = event.feature.getId();
		// infowindow.setOptions({
		// 	content: '<div style="width:' + document.getElementById('map').clientWidth + '">' + event.feature.getId() + '</div>',
		// 	position: event.feature.getGeometry().get()
		// });
		// infowindow.open(map)
		var link = location.href.split('map.html', 1)[0];
		link = link.concat('locations/', event.feature.getId(), '.html');
		//console.log(link);
		location.href = link;
	});

	var legend = document.getElementById('legend');
	for (var key in pins) {
		var div = document.createElement('div');
        div.innerHTML = '<svg width="20" height="20"><circle cx="10" cy="10" r="8"' + 
        				'fill="' + pins[key][0] + '" stroke="' + pins[key][1] + '" stroke-width="2" /></svg> ' + pins[key][2];
        legend.appendChild(div);
	}

	map.controls[google.maps.ControlPosition.LEFT_TOP].push(document.getElementById('legend'));
}