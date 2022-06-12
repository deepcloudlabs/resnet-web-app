class ViewModel {
    constructor() {
        this.results = ko.observableArray([]);
        this.fileData = ko.observable({
            dataUrl: ko.observable(AppConfig.NO_IMAGE)
        })
    }

    classifyImage = () => {
        fetch(
            `${AppConfig.REST_API_BASE_URL}`,
            {
                method: "POST",
                body: JSON.stringify({input_image: toRawImage(this.fileData().dataUrl())}),
                headers: new Headers({"Content-Type": "application/json", "Accept": "application/json"})
            }
        ).then(res => res.json())
            .then(result => {
            toastr.success("Classification is done.");
            result.image = this.fileData().dataUrl();
            this.results.push(result);
        })
            .catch(toastr.error);
    }

};

let viewModel= new ViewModel();

$(
    () => {
        ko.applyBindings(viewModel);
    }
);