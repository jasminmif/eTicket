(function() {
	var app = angular.module('app');
	app.controller('GenerateTicketController', function($scope, Request, $timeout) {
		
		$scope.generateTickets = function() {
			var generateTifcketConfirm = confirm('Are your sure you want to generate tickets ?');

			if (generateTifcketConfirm) {
				var postData = {
				};

				Request('POST', '/ticket/generate_ticket_images/', postData)
				.then(function(response) {
					alert(response.msg);
				});
			}
		};
	});
})();