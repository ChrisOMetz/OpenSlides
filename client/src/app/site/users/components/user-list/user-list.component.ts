import { Component, OnInit } from '@angular/core';
import { Title } from '@angular/platform-browser';
import { TranslateService } from '@ngx-translate/core';
import { CsvExportService } from '../../../../core/services/csv-export.service';

import { ViewUser } from '../../models/view-user';
import { UserRepositoryService } from '../../services/user-repository.service';
import { ListViewBaseComponent } from '../../../base/list-view-base';
import { Router, ActivatedRoute } from '@angular/router';
import { MatSnackBar } from '@angular/material';

/**
 * Component for the user list view.
 *
 */
@Component({
    selector: 'os-user-list',
    templateUrl: './user-list.component.html',
    styleUrls: ['./user-list.component.scss']
})
export class UserListComponent extends ListViewBaseComponent<ViewUser> implements OnInit {
    /**
     * The usual constructor for components
     *
     * @param titleService Serivce for setting the title
     * @param translate Service for translation handling
     * @param matSnackBar Helper to diplay errors
     * @param repo the user repository
     * @param router the router service
     * @param route the local route
     * @param csvExport CSV export Service
     */
    public constructor(
        titleService: Title,
        translate: TranslateService,
        matSnackBar: MatSnackBar,
        private repo: UserRepositoryService,
        private router: Router,
        private route: ActivatedRoute,
        protected csvExport: CsvExportService
    ) {
        super(titleService, translate, matSnackBar);
    }

    /**
     * Init function
     *
     * sets the title, inits the table and calls the repo
     */
    public ngOnInit(): void {
        super.setTitle('Users');
        this.initTable();
        this.repo.getViewModelListObservable().subscribe(newUsers => {
            this.dataSource.data = newUsers;
        });
    }

    /**
     * Navigate to import page or do it inline
     *
     * TODO: implement importing of users
     */
    public import(): void {
        console.log('click on Import');
    }

    /**
     * Handles the click on a user row
     *
     * @param row selected row
     */
    public selectUser(row: ViewUser): void {
        this.router.navigate([`./${row.id}`], { relativeTo: this.route });
    }

    /**
     * Handles the click on the plus button
     */
    public onPlusButton(): void {
        this.router.navigate(['./new'], { relativeTo: this.route });
    }

    /**
     * Export all users as CSV
     */
    public csvExportUserList(): void {
        this.csvExport.export(
            this.dataSource.data,
            [
                { property: 'title' },
                { property: 'first_name', label: 'Given name' },
                { property: 'last_name', label: 'Surname' },
                { property: 'structure_level', label: 'Structure level' },
                { property: 'participant_number', label: 'Participant number' },
                { property: 'groups', assemble: 'name' },
                { property: 'comment' },
                { property: 'is_active', label: 'Is active' },
                { property: 'is_present', label: 'Is present' },
                { property: 'is_committee', label: 'Is a committee' },
                { property: 'default_password', label: 'Initial password' },
                { property: 'email' }
            ],
            this.translate.instant('Participants') + '.csv'
        );
    }
}
