/* Contact Form Script */

(function() {

	"use strict";

	var newsletterForm = {

		initialized: false,

		initialize: function() {

			if (this.initialized) return;
			this.initialized = true;

			this.build();
			this.events();

		},

		build: function() {

			this.validations();

		},

		events: function() {



		},

		validations: function() {

			var newsletterform = $("#newsletter-form"),
				url = newsletterform.attr("action");

			newsletterform.validate({
				submitHandler: function(form) {

					// Loading State
					var submitButton = $(this.submitButton);
					submitButton.button("loading");

					// Ajax Submit
					$.ajax({
						type: "POST",
						url: url,
						data: {
							"email": $("#newsletter-form #email").val()
						},
						dataType: "json",
						success: function (data) {
							if (data.response == "success") {

								$("#newsletter-alert-success").removeClass("hidden");
								$("#newsletter-alert-error").addClass("hidden");

								// Reset Form
								$("#newsletter-form .form-control")
									.val("")
									.blur()
									.parent()
									.removeClass("has-success")
									.removeClass("has-error")
									.find("label.error")
									.remove();

									if(($("#newsletter-alert-success").position().top - 80) < $(window).scrollTop()){
										$("html, body").animate({
											 scrollTop: $("#newsletter-alert-success").offset().top - 80
										}, 300);
									}

							} else {

								$("#newsletter-alert-error").removeClass("hidden");
								$("#newsletter-alert-success").addClass("hidden");

								if(($("#newsletter-alert-error").position().top - 80) < $(window).scrollTop()){
									$("html, body").animate({
										scrollTop: $("#newsletter-alert-error").offset().top - 80
									}, 300);
								}

							}
						},
						complete: function () {
							submitButton.button("reset");
						}
					});
				},
				rules: {
					email: {
						required: true,
						email: true
					}
				},
				highlight: function (element) {
					$(element)
						.parent()
						.removeClass("has-success")
						.addClass("has-error");
				},
				success: function (element) {
					$(element)
						.parent()
						.removeClass("has-error")
						.addClass("has-success")
						.find("label.error")
						.remove();
				}
			});

		}

	};

	newsletterForm.initialize();

})();