(function() {
	var app = angular.module('app');
	app.controller('MainController', function($scope, Request, $timeout) {
		$scope.logs = [];

		$scope.data = {
			ticketUUID: null,
			flashSuccess: false, 
			flashError: false,
			errorMessage: '',
			playSuccessSound: true,
			playErrorSound: true
		};

		$scope.resetFlagsAndMessage = function() {
			$scope.data.flashSuccess = false;
			$scope.data.flashError = false;
			$scope.data.errorMessage = '';
		};

		$scope.scanTicket = function() {
			$scope.resetFlagsAndMessage();
			
			var postData = {
				ticketUUID: $scope.data.ticketUUID
			};

			Request('POST', '/ticket/scan_ticket/', postData)
			.then(function(response) {
				$scope.data.ticketUUID = '';
				$scope.logs.push(response);
				
				if (response.success) {
					flashSuccess();
					playSuccessSound();
				} else {
					$scope.data.errorMessage = response.msg;
					flashError();
					playErrorSound();
				}

				$timeout(function() {
					scrollPreTag();
				});
			});
		};

		var FLASH_TIMER = 2000;
		function flashSuccess() {
			$scope.data.flashSuccess = true;
		}

		function flashError() {
			$scope.data.flashError = true;
		}

		var successAudio = new Audio('./static/assets/audio/success-sound-effect.mp3');
		function playSuccessSound() {
			if ($scope.data.playSuccessSound) {
				successAudio.play();
			}
		}

		var errorAudio = new Audio('./static/assets/audio/error-sound-effect.mp3');
		function playErrorSound() {
			if ($scope.data.playErrorSound) {
				errorAudio.play();
			}
		}

		function scrollPreTag() {
			var pre = $("#logs");
    		pre.scrollTop( pre.prop("scrollHeight") );
		}
	});
})();