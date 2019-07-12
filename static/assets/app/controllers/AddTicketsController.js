(function() {
	var app = angular.module('app');
	app.controller('AddTicketsController', function($scope, Request, $timeout) {
		
		$scope.numberOfTickets = 0;

		$scope.createTickets = function() {
			var addTicketConfirm = confirm('Are your sure you want to add new ticket UUIDs ?');

			if (addTicketConfirm) {
				var postData = {
					numberOfTickets: $scope.numberOfTickets
				};

				Request('POST', '/ticket/add_ticket/', postData)
				.then(function(response) {
					alert(response.msg);
				});
			}
		};
	});
})();