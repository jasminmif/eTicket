/*
* Author: Jasmin miftari
* Date: 25/02/2016
*/

var base_url = 'http://127.0.0.1:8000/';
app.factory('Request', ['$http', '$rootScope', function($http, $rootScope) {
	return function(type, url, postData) {

		$(".spinner").show();

		return $http({
			method: type,
			url: base_url + url,
			data: postData,
		}).then(function successCallback(response){
			return response.data;
		}, function errorCallback(response){
			return response;
		});
	};
}]);

app.factory('RequestMsg', function($http, $rootScope){
	return function(type, url, postData) {
		$(".spinner").show();
		return $http({
			method: type,
			url: base_url + url,
			data: postData,
		}).then(function successCallback(response){
			$(".spinner").hide();
			return response.data;
		}, function errorCallback(response){
			$(".spinner").hide();
			if(response.data && response.data.status == 401){
				$location.path('/login');
			}else{
				return response.data;
			}
		});
	};
});